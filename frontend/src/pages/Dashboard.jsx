import React from 'react';
import PerformanceChart from '../components/PerformanceChart';
import { Typography } from '@mui/material';

const Dashboard = () => {
  return (
    <div>
      <Typography variant="h4" gutterBottom>
        Dashboard Overview
      </Typography>
      <PerformanceChart />
    </div>
  );
};

export default Dashboard;
