"use client";

import React, { useState } from 'react';

const Chat = () => {
  const [messages, setMessages] = useState<Array<{ user: string; bot?: string }>>([]);
  const [input, setInput] = useState<string>('');
  const [loading, setLoading] = useState<boolean>(false); // New loading state

  // Function to send a message
  const handleSend = async () => {
    if (!input.trim()) return;

    setMessages([...messages, { user: input }]);
    setInput('');  // Clear input immediately
    setLoading(true);  // Set loading to true while waiting for bot response

    try {
      // Call the FastAPI backend to get the bot's response
      const res = await fetch('http://localhost:8000/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: input }),
      });

      const data = await res.json();
      // Save both the user's message and bot's HTML response
      setMessages((prevMessages) => [...prevMessages, { user: input, bot: data.response }]);
    } catch (error) {
      console.error('Error sending message:', error);
    } finally {
      setLoading(false);  // Set loading to false once the response is received
    }
  };

  // Handle the Enter key press
  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter') {
      e.preventDefault(); // Prevent the default behavior (form submission)
      handleSend();       // Call handleSend to send the message
    }
  };

  return (
    <div className="w-full max-w-4xl mx-auto p-4 h-screen flex flex-col">
      {/* Title */}
      <h1 className="text-2xl font-bold text-center mb-4">Briefly</h1>

      {/* Chat window */}
      <div className="flex-grow border border-gray-300 rounded-lg p-4 overflow-y-auto bg-white h-[calc(100vh-150px)]">
        {messages.map((message, index) => (
          <div key={index} className="mb-4">
            <div><strong>User:</strong> {message.user}</div>
            {/* Render bot's HTML safely */}
            {message.bot && (
              <div
                className="mt-2"
                dangerouslySetInnerHTML={{ __html: message.bot }}  // Render HTML content
              />
            )}
          </div>
        ))}
        {/* Loading dots displayed when the bot is generating a response */}
        {loading && (
          <div className="flex items-center space-x-2 mt-2">
            <span>Briefly is typing:</span>
            <div className="dot-flashing"></div>
          </div>
        )}
      </div>

      {/* Input box */}
      <div className="flex mt-4">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}  // Update input field state
          onKeyDown={handleKeyPress}                 // Listen for Enter key press
          className="flex-grow p-2 border border-gray-300 rounded-lg"
        />
        <button
          onClick={handleSend}                       // Call handleSend on click
          className="ml-2 p-2 bg-blue-500 text-white rounded-lg"
        >
          Send
        </button>
      </div>
    </div>
  );
};

export default Chat;
