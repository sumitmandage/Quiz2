import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import EmployeeTable from './components/EmployeeTable';
import PerformanceChart from './components/PerformanceChart';
import Dashboard from './pages/Dashboard';
import AttendancePage from './pages/AttendancePage';

function App() {
  return (
    <Router>
      <Navbar />
      <div className="container my-5">
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/employees" element={<EmployeeTable />} />
          <Route path="/performance" element={<PerformanceChart />} />
          <Route path="/attendance" element={<AttendancePage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
