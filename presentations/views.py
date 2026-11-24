from django.shortcuts import render
from django.http import HttpResponse

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

from io import BytesIO


def index(request):
    return render(request, 'presentations.html')


def generate_presentation(request):

    if request.method == 'POST':

        # Get the lyrics submitted through the HTML form
        lyrics = request.POST.get('lyrics', '').strip()

        # Check whether the user entered any lyrics
        if not lyrics:
            return render(request, 'presentations.html', {
                'error': 'Please enter some lyrics.'
            })

        # Divide the lyrics into separate slides using ---
        slides_content = [
            slide.strip()
            for slide in lyrics.split('---')
            if slide.strip()
        ]

        # Get the presentation settings from the form
        font = request.POST.get('font', 'Arial')
        font_size = request.POST.get('font_size', '36')
        background = request.POST.get('background', 'black')
        text_color = request.POST.get('text_color', 'white')

        # Validate the font size
        try:
            font_size = int(font_size)
            if font_size not in [32, 36, 40, 44]:
                font_size = 36
        except ValueError:
            font_size = 36

        # Define background colors
        background_colors = {
            'black': RGBColor(0, 0, 0),
            'dark': RGBColor(20, 20, 25),
            'white': RGBColor(255, 255, 255),
        }

        # Define text colors
        text_colors = {
            'white': RGBColor(255, 255, 255),
            'black': RGBColor(0, 0, 0),
            'gold': RGBColor(220, 190, 120),
        }

        # Create a new PowerPoint presentation
        presentation = Presentation()

        # Set slide dimensions to widescreen (16:9)
        presentation.slide_width = Inches(13.333)
        presentation.slide_height = Inches(7.5)

        # Create one slide for each section of lyrics
        for slide_text in slides_content:

            # Create a blank slide
            slide = presentation.slides.add_slide(
                presentation.slide_layouts[6]
            )

            # Set the background color
            slide.background.fill.solid()
            slide.background.fill.fore_color.rgb = (
                background_colors.get(background, RGBColor(0, 0, 0))
            )

            # Create a text box
            text_box = slide.shapes.add_textbox(
                Inches(0.8),
                Inches(0.8),
                Inches(11.733),
                Inches(5.9)
            )

            text_frame = text_box.text_frame
            text_frame.word_wrap = True
            text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

            # Insert the lyrics
            text_frame.text = slide_text

            # Format the lyrics
            for paragraph in text_frame.paragraphs:

                paragraph.alignment = PP_ALIGN.CENTER

                for run in paragraph.runs:
                    run.font.name = font
                    run.font.size = Pt(font_size)
                    run.font.color.rgb = (
                        text_colors.get(text_color, RGBColor(255, 255, 255))
                    )

        # Save the presentation in memory
        output = BytesIO()
        presentation.save(output)
        output.seek(0)

        # Return the PowerPoint file as a download
        response = HttpResponse(
            output.getvalue(),
            content_type='application/vnd.openxmlformats-officedocument.presentationml.presentation'
        )

        response['Content-Disposition'] = (
            'attachment; filename="selah_presentation.pptx"'
        )

        return response

    return render(request, 'presentations.html')


def user_dashboard(request):
    return render(request, 'dashboard.html')
