use pyo3::prelude::*;
use pyo3::wrap_pyfunction;
use std::backtrace;
use std::io::{self, Write};

#[pyfunction]
fn printrs(a: &str,end: &str) -> PyResult<()> {
    print!("{}{}", a,end);
    io::stdout().flush().unwrap();
    Ok(())
}
#[pymodule]
fn core(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(printrs, m)?)?;
    Ok(())
}
