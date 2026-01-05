from pyscript import document

#define computation():
    s1 = float(document.getElementById("score1").value)
    s2 = float(document.getElementById("score2").value)

    average = (score1 + score2) / 2

    Element("average").write(f"{average:.2f}")

    if average >= 75:
        Element("result").write("Yes")
    else:
        Element("result").write("No")
