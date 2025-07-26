import React, { useState } from 'react';

const UserInput = ({ onSend }) => {
  const [text, setText] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    onSend(text);
    setText('');
  };

  return (
    <form className="user-input" onSubmit={handleSubmit}>
      <input
        type="text"
        value={text}
        placeholder="Type your message..."
        onChange={(e) => setText(e.target.value)}
      />
      <button type="submit">Send</button>
    </form>
  );
};

export default UserInput;
