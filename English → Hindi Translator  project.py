# Install required libraries
!pip -q install googletrans==4.0.0-rc1 ipywidgets

import ipywidgets as widgets
from IPython.display import display, HTML
from googletrans import Translator

# Translator object
translator = Translator()

# Translation history list
history = []

# Title
title = widgets.HTML(
    "<h1 style='color:#2E86C1;text-align:center;'>🌍 English → Hindi Translator</h1>"
)

subtitle = widgets.HTML(
    "<h4 style='text-align:center;color:gray;'>Type an English word and get its Hindi meaning instantly</h4>"
)

# Input box
english_input = widgets.Text(
    placeholder='Type English word here...',
    description='Word:',
    layout=widgets.Layout(width='400px')
)

# Buttons
translate_button = widgets.Button(
    description="🔍 Translate",
    button_style='primary',
    layout=widgets.Layout(width='150px')
)

clear_button = widgets.Button(
    description="🧹 Clear",
    button_style='warning',
    layout=widgets.Layout(width='150px')
)

delete_history_button = widgets.Button(
    description="🗑 Delete History",
    button_style='danger',
    layout=widgets.Layout(width='170px')
)

# Output areas
output = widgets.Output()
history_box = widgets.Output()

# Translate function
def translate_word(b):
    word = english_input.value

    with output:
        output.clear_output()

        if word.strip() == "":
            display(HTML("<p style='color:red;font-size:16px;'>⚠ Please enter a word</p>"))
        else:
            try:
                translated = translator.translate(word, src='en', dest='hi')
                result = translated.text

                history.append((word, result))

                display(HTML(
                    f"""
                    <div style="
                    padding:12px;
                    font-size:20px;
                    color:#1B4F72;
                    background-color:#EAF2F8;
                    border-radius:8px;">
                    <b>English:</b> {word} <br>
                    <b>Hindi:</b> {result}
                    </div>
                    """
                ))

                show_history()

            except:
                display(HTML("<p style='color:red;'>Translation error. Try again.</p>"))

# Clear input function
def clear_text(b):
    english_input.value = ""
    with output:
        output.clear_output()

# Delete history function
def delete_history(b):
    global history
    history = []
    with history_box:
        history_box.clear_output()
        display(HTML("<p style='color:red;font-size:16px;'>History Deleted ✔</p>"))

# History display
def show_history():
    with history_box:
        history_box.clear_output()

        if history:
            display(HTML("<h3 style='color:#117864'>📜 Translation History</h3>"))

            for eng, hin in history:
                display(HTML(
                    f"<p style='font-size:16px;'><b>{eng}</b> → {hin}</p>"
                ))

# Button actions
translate_button.on_click(translate_word)
clear_button.on_click(clear_text)
delete_history_button.on_click(delete_history)

# Button layout
button_box = widgets.HBox([translate_button, clear_button, delete_history_button])

# Display UI
display(title)
display(subtitle)
display(english_input)
display(button_box)
display(output)

display(history_box)



