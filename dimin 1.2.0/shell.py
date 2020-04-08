
import dimin
import colorama

colorama.init(convert=True)

print(colorama.Fore.GREEN + 'Shell' + colorama.Style.RESET_ALL)

while True:
    try:
        print(colorama.Fore.GREEN + "dimin > " + colorama.Fore.LIGHTMAGENTA_EX, end="")
        text = input('')
        print(colorama.Style.RESET_ALL, end="")
    except BaseException:
        text = ""
    result, error = dimin.run('<shell>', text)

    # if error: print(error.as_string())
    if error: print(colorama.Fore.RED + error.as_string() + colorama.Style.RESET_ALL)
    elif result: print(colorama.Fore.BLUE + str(result) + colorama.Style.RESET_ALL)