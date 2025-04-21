// import React, { useEffect, useState } from 'react';
// import axios from 'axios';
// import { Bar } from 'react-chartjs-2';
// import { Chart as ChartJS, BarElement, CategoryScale, LinearScale, Tooltip, Legend } from 'chart.js';

// ChartJS.register(BarElement, CategoryScale, LinearScale, Tooltip, Legend);

// function PerformanceChart() {
//   const [chartData, setChartData] = useState({});

//   useEffect(() => {
//     axios.get('http://localhost:5000/performance-summary').then((res) => {
//       const labels = Object.keys(res.data);
//       const values = Object.values(res.data);

//       setChartData({
//         labels,
//         datasets: [
//           {
//             label: 'Avg Performance Score',
//             data: values,
//             backgroundColor: 'rgba(54, 162, 235, 0.6)',
//           },
//         ],
//       });
//     });
//   }, []);

//   return (
//     <div>
//       <h2>Performance Summary</h2>
//       {chartData.labels ? <Bar data={chartData} /> : <p>Loading chart...</p>}
//     </div>
//   );
// }

// export default PerformanceChart;


import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Bar } from 'react-chartjs-2';
import { Table } from 'react-bootstrap';
import {
  Chart as ChartJS,
  BarElement,
  CategoryScale,
  LinearScale,
  Tooltip,
  Legend,
} from 'chart.js';

ChartJS.register(BarElement, CategoryScale, LinearScale, Tooltip, Legend);

const PerformanceChart = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5000/performance')
      .then((res) => setData(res.data))
      .catch((err) => console.error(err));
  }, []);

  const chartData = {
    labels: data.map((item) => item.employee_name),
    datasets: [
      {
        label: 'Performance Score',
        data: data.map((item) => item.score),
        backgroundColor: '#007bff',
      },
    ],
  };

  return (
    <div>
      <h2 className="mb-4">Employee Performance</h2>

      <div className="mb-5">
        <Bar data={chartData} />
      </div>

      <h4>Performance Details</h4>
      <Table striped bordered hover responsive>
        <thead>
          <tr>
            <th>#</th>
            <th>Employee</th>
            <th>Score</th>
            <th>Review Date</th>
            <th>Feedback</th>
          </tr>
        </thead>
        <tbody>
          {data.map((perf, index) => (
            <tr key={perf.id}>
              <td>{index + 1}</td>
              <td>{perf.employee_name}</td>
              <td>{perf.score}</td>
              <td>{perf.review_date}</td>
              <td>{perf.remarks}</td>
            </tr>
          ))}
        </tbody>
      </Table>
    </div>
  );
};

export default PerformanceChart;
