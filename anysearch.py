# import openai library
import openai
#import tkinter library for frameworks
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.font import Font
from PIL import Image,ImageTk
#importing gtts and playsound for generating audio response
import gtts
import playsound
def getInfo():
    model_engine = "text-davinci-003"
    prompt = t.get()
    #print(prompt)
    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    # extracting useful part of response
    response = completion.choices[0].text
    # printing response
    #print(response)

    t1.insert(tk.END, response)
    #creating a audio response of the entered query
    # sound=gtts.gTTS(response,lang="en")
    # sound.save("voice.mp3")
    # playsound.playsound("voice.mp3")
# Set up the OpenAI API client

openai.api_key = "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"

window = tk.Tk()
window.title("AnySearch")
window.configure(background="grey")
window.iconbitmap("Project Work\iconA.ico")
ttk.Label(window,text="AI SEARCH TOOL",background="grey",foreground="black",font="comicsansms 36 bold", borderwidth=3).grid(
    row=0,column=0,padx=10,pady=25,ipadx=10,ipady=10
)
# photo=tk.PhotoImage(name='image_1',file="Project Work\icon.png")
# image_label=tk.Label(window,image=photo).grid(row=0,column=2,padx=10,pady=25,ipadx=10,ipady=10)
image=Image.open("Project Work\icon.png")
image=image.resize((100,100))
imagenew=ImageTk.PhotoImage(image)
imagelabel=ttk.Label(window,image=imagenew,background="grey").grid(row=0,column=1,padx=10,pady=25,ipadx=10,ipady=10)
ttk.Label(window, text="Ask Anything :",
          font=("Times New Roman 22 bold", 15),background="grey",foreground="black").grid(
  column=0, row=2, padx=10, pady=25)

# Text Widget
t = tk.Entry(window, width=20)
  
t.grid(column=1, row=2)
'''
widgets are added here
'''
b = tk.Button(window,text="Click",command=getInfo)
  
b.grid(columnspan=2, row=3)

t1 = tk.Text(window,  height=20, width=100,bg='white') # added one text box
t1.grid(row=25,columnspan=2) 

window.mainloop()