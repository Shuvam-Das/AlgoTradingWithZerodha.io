import React, { useEffect } from 'react';
import io from 'socket.io-client';

const Dashboard = () => {
  useEffect(() => {
    const socket = io('http://localhost:8000');

    socket.on('connect', () => {
      console.log('Connected to socket server');
    });

    socket.on('disconnect', () => {
      console.log('Disconnected from socket server');
    });

    return () => {
      socket.disconnect();
    };
  }, []);

  return (
    <div className="flex items-center justify-center h-screen bg-gray-100">
      <h1 className="text-3xl font-bold">Welcome to your Dashboard</h1>
    </div>
  );
};

export default Dashboard;