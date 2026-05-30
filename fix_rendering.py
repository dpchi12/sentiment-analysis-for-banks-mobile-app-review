import nbformat

def strip_base64_outputs(path):
    nb = nbformat.read(path, as_version=4)
    for cell in nb.cells:
        if cell.cell_type == "code":
            new_outputs = []
            for output in cell.outputs:
                if output.get("output_type") in ("display_data", "execute_result"):
                    data = output.get("data", {})
                    data.pop("image/png", None)
                    data.pop("image/jpeg", None)
                    data.pop("image/svg+xml", None)
                    output["data"] = data
                new_outputs.append(output)
            cell.outputs = new_outputs
    nbformat.write(nb, path)
    print(f"done: {path}")

strip_base64_outputs("Model (old data)/old_approach_sentiment_analysis.ipynb")
strip_base64_outputs("Model (old data)/old_preprocessing.ipynb")
strip_base64_outputs("Model (new data)/new_preprocessing.ipynb")
