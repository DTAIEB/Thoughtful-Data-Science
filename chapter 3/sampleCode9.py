def compute_pdf(key):
    return pandas.DataFrame([
        {"col{}".format(i): "{}{}-{}".format(key,i,j) for i in range(4)} for j in range(10)
    ])
