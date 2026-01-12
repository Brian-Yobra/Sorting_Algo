use pyo3::prelude::*;

// This function performs the actual sorting logic
fn recursive_merge_sort(arr: &mut [i32]) {
    let n = arr.len();
    if n <= 1 {
        return;
    }
    let mid = n / 2;

    // Sort the left and right halves in-place using slices
    recursive_merge_sort(&mut arr[..mid]);
    recursive_merge_sort(&mut arr[mid..]);

    // Merge the two sorted halves
    let mut temp = Vec::with_capacity(n);
    let mut i = 0;
    let mut j = mid;

    while i < mid && j < n {
        if arr[i] <= arr[j] {
            temp.push(arr[i]);
            i += 1;
        } else {
            temp.push(arr[j]);
            j += 1;
        }
    }

    // Push remaining elements
    temp.extend_from_slice(&arr[i..mid]);
    temp.extend_from_slice(&arr[j..n]);

    // Copy back to original array
    arr.copy_from_slice(&temp);
}

// This is the function exposed to Python
#[pyfunction]
fn merge_sort(mut arr: Vec<i32>) -> PyResult<Vec<i32>> {
    recursive_merge_sort(&mut arr);
    Ok(arr)
}

// The module name "rust_sort" MUST match the lib.name in Cargo.toml
#[pymodule]
fn rust_sort(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(merge_sort, m)?)?;
    Ok(())
}
