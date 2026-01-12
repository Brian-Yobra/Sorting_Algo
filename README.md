### Sorting Algorith 

# Python vs Rust: Sorting Benchmark

```markdown

A project exploring the performance gap between **Interpreted Python**, **C-optimized Python (Timsort)**, and **Compiled Rust**.

## Requirements
- **Rust**: `cargo` 1.70+
- **Python**: `3.13`
- **Maturin**: `pip install maturin`

## Installation & Build

1. **Clone the project** and navigate to the directory.
2. **Setup Virtual Environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate

```

3. **Compile Rust for Python**:
```bash
# Use --release flag for actual performance testing!
maturin develop --release

```



## Running the Benchmark

Execute different algorithms using the command line arguments:

| Command | Algorithm | Logic |
| --- | --- | --- |
| `python3 main.py merge` | **Python Merge** | Pure Python recursion |
| `python3 main.py tim` | **Python Built-in** | Timsort (C-Engine) |
| `python3 main.py rmerge` | **Rust Merge** | Compiled Rust (Slices) |

### Example Test

```bash
time python3 main.py rmerge

```

## Performance Notes

In our tests with a large `dataset.txt`, the results were:

* **Python Merge Sort**: ~198s
* **Python Timsort**: ~29s
* **Rust Merge Sort**: ~13s (Winner)

## Configuration

The bridge is powered by **PyO3 0.23**. The Rust code is located in `src/lib.rs` and is compiled into a shared object that Python imports as a native module.

```

---

### Tips for your README:
* **Backticks (\`)**: Use these to create the grey code blocks shown above.
* **Tables**: Use pipes `|` and dashes `-` to keep your comparison data organized.
* **Bold/Italics**: Use `**text**` for bold and `*text*` for italics to highlight key terms.



**Would you like me to add a Python script that generates a random `dataset.txt` with 1 million numbers for your tests?**

```
