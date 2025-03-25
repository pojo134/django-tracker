def theme_processor(request):
    """
    Context processor to add theme preference to all templates.
    """
    theme_preference = request.session.get('theme_preference', 'medicine')
    return {
        'theme_preference': theme_preference
    }
