# TRY EXCEPTION HANDLING 
# EXCEPTION WO ERROR HOTY HAN JO RUNTIME PY ATY HA 
# try except else finally
while True:
    try: #try may have multiple ecept blocks 
        age=int(input("ENTER YOUR AGE : "))
        break
    except ValueError:
        print("may be you entered a string try again ...")
    except:
        print("unexpected input")
    else:
        print('hello')
    finally:
        print("ahfshsd")

