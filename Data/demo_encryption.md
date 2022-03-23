---
jupyter:
  interpreter:
    hash: bb04143b76cf4aa8b010820e1498da26f1eeac71d04edabfea3b39816255051b
  kernelspec:
    display_name: "Python 3.8.12 64-bit (\\'main_env1\\': conda)"
    name: python3
  language_info:
    codemirror_mode:
      name: ipython
      version: 3
    file_extension: .py
    mimetype: text/x-python
    name: python
    nbconvert_exporter: python
    pygments_lexer: ipython3
    version: 3.8.12
  nbformat: 4
  nbformat_minor: 2
  orig_nbformat: 4
---

::: {.cell .markdown}
# CSV
:::

::: {.cell .code execution_count="73"}
``` {.python}
import pandas as pd
```
:::

::: {.cell .code execution_count="74"}
``` {.python}
data = pd.read_csv('encryption.csv')
```
:::

::: {.cell .code execution_count="149"}
``` {.python}
def encrypt(input_text):
    new_text = ''
    upper_code = ''

    for character in input_text.upper():
        new_text += data[data['Letter'] == character]['Code'].iloc[0] + '!~!'
    
    for character in input_text:
        upper_code += str(int(character.isupper()))

    return new_text, upper_code
```
:::

::: {.cell .code execution_count="154"}
``` {.python}
def decrypt(output_text, output_code):
    output_text = output_text.replace('!~!', ' ')
    text_list = output_text.split()
    
    original_text = ''
    final_text = ''
    
    for text in text_list:
        original_text += data[data['Code'] == text]['Letter'].iloc[0]

    out = original_text.lower()
    for i in range(len(out)):
        if output_code[i] == '1':
            final_text += out[i].upper()
        else:
            final_text += out[i]
    
    return final_text
```
:::

::: {.cell .code execution_count="169"}
``` {.python}
input_text = input()

print(input_text,'\n')

a, b = encrypt(input_text)

print(a, f'\n{b}\n')

print(decrypt(a, b))
```

::: {.output .stream .stdout}
    Veer Sandhu 

    {]]]JF&8!~!^*#K;FSD!~!^*#K;FSD!~!%%**HJU!~!(^#&(#!~!WA&*QWE!~!SD#*(H!~!#@(JLKJ!~!RET&*!~!F\GDS[!~!SAK**(!~! 
    10000100000

    Veer Sandhu
:::
:::

::: {.cell .markdown}
# JSON
:::

::: {.cell .code execution_count="1"}
``` {.python}
import json
```
:::

::: {.cell .code execution_count="3"}
``` {.python}
path = 'key_val.json'
with open(path) as f:
    data_json = json.load(f)
```
:::

::: {.cell .code execution_count="28"}
``` {.python}
def encrypt2(input_text):
    new_text = ''
    upper_code = ''

    for character in input_text.upper():
        for i in range(len(data_json)):
            if (data_json[i]['Letter'] == character):
                new_text += (data_json[i]['Code']) +'!~!'
    
    for character in input_text:
        upper_code += str(int(character.isupper()))

    return new_text, upper_code
```
:::

::: {.cell .code execution_count="29"}
``` {.python}
def decrypt2(output_text, output_code):
    output_text = output_text.replace('!~!', ' ')
    text_list = output_text.split()
    
    original_text = ''
    cased_text = ''
    
    for text in text_list:
        for i in range(len(data_json)):
            if (data_json[i]['Code'] == text):
                original_text += (data_json[i]['Letter'])


    out = original_text.lower()
    for i in range(len(out)):
        if output_code[i] == '1':
            cased_text += out[i].upper()
        else:
            cased_text += out[i]
    
    return cased_text
```
:::

::: {.cell .code execution_count="31"}
``` {.python}
input_text2 = input()

print(input_text2,'\n')

a2, b2 = encrypt2(input_text2)

print(a2, f'\n{b2}\n')

print(decrypt2(a2, b2))
```

::: {.output .stream .stdout}
    Veer Sandhu 

    {]]]JF&8!~!^*#K;FSD!~!^*#K;FSD!~!%%**HJU!~!(^#&(#!~!WA&*QWE!~!SD#*(H!~!#@(JLKJ!~!RET&*!~!F\GDS[!~!SAK**(!~! 
    10000100000

    Veer Sandhu
:::
:::
