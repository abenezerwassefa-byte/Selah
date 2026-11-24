from django.shortcuts import render


def index(request):
    return render(request, 'presentations.html')


def generate_presentation(request):

    if request.method == 'POST':

        # Get the submitted lyrics
        lyrics = request.POST.get('lyrics', '').strip()

        # Validate the lyrics
        if not lyrics:
            return render(request, 'presentations.html', {
                'error': 'Please enter some lyrics.'
            })

        # Divide lyrics into slides
        slides = [
            slide.strip()
            for slide in lyrics.split('---')
            if slide.strip()
        ]

        # Get presentation settings
        font = request.POST.get('font', 'Arial')
        font_size = request.POST.get('font_size', '36')
        background = request.POST.get('background', 'black')
        text_color = request.POST.get('text_color', 'white')

        # Validate font size
        try:
            font_size = int(font_size)
            if font_size not in [32, 36, 40, 44]:
                font_size = 36
        except ValueError:
            font_size = 36

        # Send everything to the viewer
        return render(request, 'viewer.html', {
            'slides': slides,
            'font': font,
            'font_size': font_size,
            'background': background,
            'text_color': text_color,
        })

    return render(request, 'presentations.html')


def user_dashboard(request):
    return render(request, 'dashboard.html')


def viewer(request):
    slides = [
        "Amazing grace, how sweet the sound",
        "That saved a wretch like me",
        "I once was lost, but now am found",
    ]

    return render(request, 'viewer.html', {
        'slides': slides
    })
