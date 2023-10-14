import logo from './logo.svg';
import './App.css';
// frontend/src/App.js

import React from "react";
import {
  BrowserRouter as Router,
  Route,
  Switch
} from "react-router-dom";

function App() {
  return (
    <Router>
      <Switch>
        <Route path="/login">
          <Login />
        </Route>
        <Route path="/register">
          <Register />
        </Route>
        <Route path="/movies">
          {/* Movie Display Page Component */}
        </Route>
        <Route path="/matches">
          {/* Matches Page Component */}
        </Route>
        <Route path="/">
          {/* Home Page Component */}
        </Route>
      </Switch>
    </Router>
  );
}

export default App;
