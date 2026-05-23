import os
import numpy as np
import tensorflow as tf

from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required

# LOGIN / REGISTER IMPORTS
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Native Keras model loading utilities
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Import your form model setup cleanly
from .forms import ContactForm


# =========================================================================
# MODEL PATH
# =========================================================================
MODEL_PATH = os.path.join(
    settings.BASE_DIR,
    'ml_model',
    'sipakmed_cervical_cancer_model.keras'
)


# =========================================================================
# CLASS LABELS
# =========================================================================
class_names = [
    'Dyskeratotic (Abnormal / Pre-cancerous)',
    'Koilocytotic (Abnormal / HPV Infected)',
    'Metaplastic (Benign / Normal Variation)',
    'Parabasal (Benign / Normal)',
    'Superficial-Intermediate (Benign / Normal)'
]


# =========================================================================
# HOME PAGE
# =========================================================================
@login_required
def home_view(request):

    return render(request, 'home.html')


# =========================================================================
# ABOUT PAGE
# =========================================================================
@login_required
def about_view(request):

    return render(request, 'about.html')


# =========================================================================
# CONTACT PAGE
# =========================================================================
@login_required
def contact_view(request):

    if request.method == 'POST':

        form = ContactForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Thank you! Your message has been saved successfully."
            )

            return redirect('contact')

    else:

        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


# =========================================================================
# REGISTER FUNCTION
# =========================================================================
def register_view(request):

    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # PASSWORD CHECK
        if password1 != password2:

            messages.error(request, "Passwords do not match.")

            return redirect('register')

        # USERNAME CHECK
        if User.objects.filter(username=username).exists():

            messages.error(request, "Username already exists.")

            return redirect('register')

        # CREATE USER
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )

        user.save()

        messages.success(
            request,
            "Account created successfully."
        )

        return redirect('login')

    return render(request, 'register.html')


# =========================================================================
# LOGIN FUNCTION
# =========================================================================
def login_view(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            messages.success(
                request,
                "Login successful."
            )

            return redirect('home')

        else:

            messages.error(
                request,
                "Invalid username or password."
            )

            return redirect('login')

    return render(request, 'login.html')


# =========================================================================
# LOGOUT FUNCTION
# =========================================================================
def logout_view(request):

    logout(request)

    messages.success(
        request,
        "Logged out successfully."
    )

    return redirect('login')


# =========================================================================
# AI PREDICTION FUNCTION
# =========================================================================
@login_required
def predict_view(request):

    if request.method == 'POST' and request.FILES.get('file'):

        uploaded_image = request.FILES['file']

        # SAVE IMAGE
        fs = FileSystemStorage(location=settings.MEDIA_ROOT)

        filename = fs.save(
            uploaded_image.name,
            uploaded_image
        )

        uploaded_file_url = fs.url(filename)

        absolute_file_path = fs.path(filename)

        try:

            # IMAGE PREPROCESSING
            img = image.load_img(
                absolute_file_path,
                target_size=(224, 224)
            )

            img_array = image.img_to_array(img)

            img_tensor = tf.expand_dims(img_array, 0)

            # LOAD MODEL ONLY DURING PREDICTION
            model = load_model(MODEL_PATH, compile=False)

            # MODEL PREDICTION
            prediction = model.predict(img_tensor)

            probabilities = prediction[0]

            raw_array_string = [
                f"{float(val) * 100:.1f}%"
                for val in probabilities
            ]

            predicted_index = np.argmax(probabilities)

            # CLASS LABEL
            if predicted_index < len(class_names):

                result_label = class_names[predicted_index]

            else:

                result_label = (
                    f"Unknown Cellular Index Location: "
                    f"{predicted_index}"
                )

            confidence_score = (
                f"{probabilities[predicted_index] * 100:.2f}%"
            )

            # RETURN RESULT
            return render(request, 'about.html', {

                'success_message':
                'AI Diagnostic Scanning Complete!',

                'prediction_result':
                result_label,

                'confidence':
                confidence_score,

                'analyzed_image_url':
                uploaded_file_url,

                'debug_probabilities':
                raw_array_string
            })

        except Exception as e:

            return render(request, 'about.html', {

                'error_message':
                f'Processing Engine Fault: {str(e)}'
            })

    return render(request, 'about.html', {

        'error_message':
        'No evaluation file detected.'
    })