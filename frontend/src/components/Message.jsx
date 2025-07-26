import React from 'react';

const Message = ({ sender, text }) => {
  const isUser = sender === 'user';

  return (
    <div className={`message ${isUser ? 'user' : 'ai'}`}>
      <p>{text}</p>
    </div>
  );
};

export default Message;
