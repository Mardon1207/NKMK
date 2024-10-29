document.getElementById('print').addEventListener('click', function() {
  window.print();
});

document.getElementById('exportsave').addEventListener('click', function() {
  exportTableToExcel('transactionsTable', 'table_data');
});

function exportTableToExcel(tableID, filename = ''){
  const tableSelect = document.getElementById(tableID);
  const wb = XLSX.utils.table_to_book(tableSelect, { sheet: "Sheet1" });
  const wbout = XLSX.write(wb, { bookType: 'xlsx', type: 'binary' });

  function s2ab(s) {
    const buf = new ArrayBuffer(s.length);
    const view = new Uint8Array(buf);
    for (let i = 0; i < s.length; i++) view[i] = s.charCodeAt(i) & 0xFF;
    return buf;
  }

  const blob = new Blob([s2ab(wbout)], { type: "application/octet-stream" });

  const link = document.createElement("a");
  link.href = URL.createObjectURL(blob);
  link.download = filename ? filename + ".xlsx" : "excel_data.xlsx";
  link.click();
}
  