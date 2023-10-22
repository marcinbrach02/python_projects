x, y = "0", "1"
with open("pass.txt", "w") as f:
    try:
        f.write(str(2))
        f.write(str(int(9*0.7)))
        f.write(5//2)
        f.write(9*6)
    except TypeError:
        try:
            f.write("1")
            f.write(str(2-2))
            f.write(10/0)
            f.write(5*"2")
        except TypeError:
            f.write(777)
        except ZeroDivisionError:
            f.write("2")
            try:
                f.write(x)
                f.write(x*y)
            except TypeError:
                try:
                    f.write(z)
                except TypeError:
                    f.write("10")
                except NameError:
                    f.write("20")
