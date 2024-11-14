import arrr
from pyscript import document


def translate_english(event):
    input_text = document.querySelector("#english")
    english = input_text.value
    output_div = document.querySelector("#output")
    output_div.innerText = arrr.translate(english)


print("Ya se puede crear una pagina web")
