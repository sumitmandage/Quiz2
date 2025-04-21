import React from 'react';
import { Link } from 'react-router-dom';
import { Navbar as BSNavbar, Container, Nav } from 'react-bootstrap';

const Navbar = () => {
  return (
    <BSNavbar bg="primary" variant="dark" expand="lg">
      <Container>
        <BSNavbar.Brand as={Link} to="/">Employee Dashboard</BSNavbar.Brand>
        <BSNavbar.Toggle aria-controls="basic-navbar-nav" />
        <BSNavbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link as={Link} to="/">Dashboard</Nav.Link>
            <Nav.Link as={Link} to="/employees">Employees</Nav.Link>
            <Nav.Link as={Link} to="/performance">Performance</Nav.Link>
            <Nav.Link as={Link} to="/attendance">Attendance</Nav.Link>
          </Nav>
        </BSNavbar.Collapse>
      </Container>
    </BSNavbar>
  );
};

export default Navbar;
