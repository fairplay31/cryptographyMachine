# storage file

import justpy as jp

def hello_world():
    wp = jp.WebPage()
    my_paragraph_design = "w-64 bg-blue-500 m-2 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
    jp.P(text=f'{i}) Process File with Caesar Cipher', a=wp, classes=my_paragraph_design)
    return wp



jp.justpy(hello_world())