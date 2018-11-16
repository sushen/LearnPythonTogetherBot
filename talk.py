def talking():

    greetings = 'আমি ভাল । আপনি ভাল আছেন?'

    template = []

    for greeting in greetings:
        facebook_template_Dictionary = {
            'title': greeting[greetings]
        }
        template.append(facebook_template_Dictionary)

    return template
