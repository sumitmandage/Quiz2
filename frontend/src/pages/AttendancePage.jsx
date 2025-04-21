import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Table } from 'react-bootstrap';

const AttendancePage = () => {
  const [records, setRecords] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5000/attendance')
      .then((res) => setRecords(res.data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <div>
      <h2 className="mb-4">Employee Attendance</h2>
      <Table striped bordered hover responsive>
        <thead>
          <tr>
            <th>#</th>
            <th>Employee</th>
            <th>Date</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          {records.map((r, index) => (
            <tr key={r.id}>
              <td>{index + 1}</td>
              <td>{r.employee_name}</td>
              <td>{r.date}</td>
              <td>{r.status}</td>
            </tr>
          ))}
        </tbody>
      </Table>
    </div>
  );
};

export default AttendancePage;
