# base/views.py

from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import ContactForm

def home_view(request):
    return render(request, 'base/home.html')

def about_view(request):
    return render(request, 'base/about.html')

def project_view(request):
    return render(request, 'base/project.html')
def ecommerce_detail(request):
    return render(request, 'base/ecommerce_detail.html', {
        'project_name': 'E-Commerce Shopping App',
        'description': ('This Python-based e-commerce platform was built using Django with an SQLite database. '
                        'The application features user authentication, product management, a shopping cart system, '
                        'and secure payment integration to ensure a streamlined shopping experience.')
    })

def juice_detail(request):
    return render(request, 'base/juice_detail.html', {
        'project_name': 'Juice Website',
        'description': ('For this project, I developed the frontend of a juice website using React.js for dynamic '
                        'and responsive components. Material-UI and Bootstrap were utilized to enhance the design, '
                        'ensuring a visually engaging user interface.')
    })

def portfolio_detail(request):
    return render(request, 'base/portfolio_detail.html', {
        'project_name': 'Personal Portfolio Website',
        'description': (
            'Technologies: Django, SQLite, HTML, CSS, Bootstrap, JavaScript  \n\n'
            '- Developed a personal portfolio website to showcase my projects, skills, and contact information.\n'
            '- Implemented a responsive design using Bootstrap for seamless viewing on different devices.\n'
            '- Integrated a contact form that stores user messages in a SQLite database and displays confirmation upon successful submission.\n'
            '- Utilized Django templates to create a dynamic and modular website structure.\n'
            '- Included a projects section with details on various featured projects, along with a download link for my resume.\n'
            '- Ensured the site’s functionality and aesthetic alignment with modern web development standards.\n'
            
                        
                        )
    })

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')  # Redirect to the same page or another page
    else:
        form = ContactForm()

    return render(request, 'base/contact.html', {'form': form})

