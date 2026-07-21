try:
    import Utilis

    output = Utilis.Mathematics.fibonacci(1.0, 10)
    print(output)

    output = Utilis.Mathematics.basic.add([1,2,3])
    print(output)

    output = Utilis.Mathematics.basic.substract(12, [1,2,3])
    print(output)

    output = Utilis.Mathematics.basic.multiply([1,2,3])
    print(output)
    
    output = Utilis.Mathematics.basic.devide(18.0, 3)
    print(output)

    output = Utilis.Mathematics.basic.floor(18.0, 3)
    print(output)

    output = Utilis.Mathematics.basic.modulo(16.0, 10)
    print(output)

    output = Utilis.Mathematics.basic.devideFull(18.0, 3)
    print(output)

    output = Utilis.Mathematics.kgvggt.kgv(2,3)
    print(output)

    output = Utilis.Mathematics.kgvggt.ggt(24,66)
    print(output)

    outputP = Utilis.Mathematics.periode.seeperiod(1, 3)
    print(outputP)

    output = Utilis.Mathematics.periode.seeperiod(1, 4)
    print(output)

    output = Utilis.Mathematics.periode.resolve_periode(outputP)
    print(output)

    output = Utilis.Mathematics.basic.extrapolation(2.44948974278,2)
    print(output)

    output = Utilis.Mathematics.basic.root(7)
    print(output)

    output = Utilis.Convert.var.Num.NumToDic(Utilis.Convert.var.stringToNum("Hi"))
    print(output)
    image = True
    if image == True:
        output = Utilis.Convert.image.SVGToPNG.svg_to_png(input="noodle-bowl.svg", var=True, output="ausgabe.png")
        print(output)
        try:
            image = "noodle-bowl.svg"
            import tkinter as tk
    
            root = tk.Tk()
            image = Utilis.Convert.image.SVGToPNG.svg_to_png(input=image, var=True)
            image = Utilis.Convert.image.PNGToTk.PNGToTK(png=image)
            labl = tk.Label(root, image=image, text="Image:", compound="right").pack()
            root.mainloop()
        except Exception as e:
            from tkinter import messagebox
            messagebox.showerror("Fehler", e)
    else:
        from tkinter import messagebox
        messagebox.showinfo("Fertig", "Es gab keinen fatalen Fehler!")
       
      
except Exception as e:
    from tkinter import messagebox
    messagebox.showerror("Fehler", e)
