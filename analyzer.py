# %%
import pandas as pd
from tabulate import tabulate as tb

# %%
def analyzer_printer(i, ign_val=70):

    exp = []

    print("\n\n")

    exp.append(["Dataype", df[i].dtype])

    exp.append(["Total value", len(df[i])])

    exp.append(["Total Null", df[i].isnull().sum()])

    exp.append(["Total Uniques", df[i].nunique()])

    # exp.append(['Minimum value', min(df[i])])

    # exp.append(['Maximum value', max(df[i])])

    exp.append(
        ["Percent Uniques\n[Round Figure]", round(df[i].nunique() / len(df[i]) * 100)]
    )

    exp.append(
        [
            "Might be categorical",
            "Yes" if round(df[i].nunique() / len(df[i]) * 100) <= 10 else "No",
        ]
    )

    exp.append(
        [
            "Column might be ignored\n[based on uniqueness]",
            "Yes" if round(df[i].nunique() / len(df[i]) * 100) >= ign_val else "No",
        ]
    )

    print(tb(exp, headers=["Cloumn name", i], tablefmt="fancy_grid"))


# %%
def analyzer(df, n_only=False, ign_val=70):

    if n_only == "nll":
        for i in df.columns:
            if df[i].isnull().sum() > 0:
                analyzer_printer(i)

    elif n_only == "cat":
        for i in df.columns:
            if round(df[i].nunique() / len(df[i]) * 100) <= 10:
                analyzer_printer(i)

    elif n_only == "ign":
        for i in df.columns:
            if round(df[i].nunique() / len(df[i]) * 100) >= ign_val:
                analyzer_printer(i)

    elif n_only is False:
        for i in df.columns:
            analyzer_printer(i)


# %%
fname = input("\n\nEnter filename without .csv\t") + ".csv"

df = pd.read_csv(fname)

print("\nHit Enter to skip these.........")

n_only = input("\n\nUse nll, cat or ign\t").strip()

ign_val = input("\nEnter a Threshold\t")

if ign_val == "":

    ign_val = 70

else:

    ign_val = int(ign_val)

# file_check = input(
#     "Do you want to save output as analyzer_output.txt file?\n\
#     Output wont be displayed on terminal\n\
#     File will be opened immediately\n\
#     (Y/N/Enter to skip)\t"
# )

# if file_check in ["Y", "y"]:
#     file_ = open("analyzer_output.txt", "w")
#     file_.truncate(0)
#     file_.write()
#     file_.write(analyzer(df, n_only, ign_val))
#     import webbrowser

#     webbrowser.open("analyzer_output.txt")
# else:
#     analyzer(df, n_only, ign_val)

# %%
analyzer(df, n_only, ign_val)

# %%
