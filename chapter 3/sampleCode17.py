def get_pdf(self):
    if self.show_stats:
        summary = self.pdf.describe()
        summary.insert(0, "Stat", summary.index)
        return summary
    return self.pdf
