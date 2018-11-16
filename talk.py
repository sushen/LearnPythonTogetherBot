def talking():

    greetings = 'আমি ভাল । আপনি ভাল আছেন?'

    template = []

    for greeting in greetings:
        facebook_template_Dictionary = {
            'title': greeting['title']
        }
        template.append(facebook_template_Dictionary)

    return template
