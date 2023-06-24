import ai21
def api(comment2):
    ai21.api_key = 'HfwrU4Zhl7AKCrS9Amn4Ha1aj1djvwXj'
    response=ai21.Paraphrase.execute(text=comment2)
    return(response)