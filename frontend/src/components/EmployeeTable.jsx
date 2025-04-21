


import React, { useEffect, useState } from 'react';
import axios from 'axios';
import {
  Table, TableBody, TableCell, TableContainer, TableHead, TableRow,
  Paper, Button, Typography
} from '@mui/material';

function EmployeeTable() {
  const [employees, setEmployees] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5000/employees').then((res) => {
      setEmployees(res.data);
    });
  }, []);

  const handleExportCSV = () => {
    if (!employees.length) return;

    const headers = ['Name', 'Email', 'Department', 'Joining Date', 'Salary'];
    const rows = employees.map(emp => [
      emp.name,
      emp.email,
      emp.department,
      emp.joining_date,
      emp.salary
    ]);

    const csvContent = [
      headers.join(','),
      ...rows.map(row => row.join(','))
    ].join('\n');

    const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.setAttribute('download', 'employee_data.csv');
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  return (
    <div style={{ marginTop: '30px' }}>
      <Typography variant="h5" gutterBottom>
        Employees
      </Typography>

      <Button variant="contained" color="primary" onClick={handleExportCSV} sx={{ mb: 2 }}>
        Download Employee CSV
      </Button>

      <TableContainer component={Paper} elevation={3}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell><strong>Name</strong></TableCell>
              <TableCell><strong>Email</strong></TableCell>
              <TableCell><strong>Department</strong></TableCell>
              <TableCell><strong>Joining Date</strong></TableCell>
              <TableCell><strong>Salary</strong></TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {employees.map((emp) => (
              <TableRow key={emp.id}>
                <TableCell>{emp.name}</TableCell>
                <TableCell>{emp.email}</TableCell>
                <TableCell>{emp.department}</TableCell>
                <TableCell>{emp.joining_date}</TableCell>
                <TableCell>${emp.salary}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </div>
  );
}

export default EmployeeTable;
