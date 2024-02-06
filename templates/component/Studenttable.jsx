// myComponent.jsx
import React from 'react';
import ReactDOM from 'react-dom';
import { Table, TableHead, TableBody, TableRow, TableCell } from '@mui/material';

const MyComponent = ({ students }) => (
  <div>
    <h1>Hello Python</h1>
    <Table>
      <TableHead>
        <TableRow>
          <TableCell align="right">Name</TableCell>
          <TableCell align="right">Age</TableCell>
          <TableCell align="right">Address</TableCell>
        </TableRow>
      </TableHead>
      <TableBody>
        {students.map((row) => (
          <TableRow key={row.name}>
            <TableCell align="right">{row.name}</TableCell>
            <TableCell align="right">{row.age}</TableCell>
            <TableCell align="right">{row.address}</TableCell>
          </TableRow>
        ))}
      </TableBody>
    </Table>
  </div>
);

ReactDOM.render(<MyComponent students={students} />, document.getElementById('root'));
