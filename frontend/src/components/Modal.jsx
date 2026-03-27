const Modal = ({ children }) => {
  return (
    <div style={{ background: "rgba(0,0,0,0.5)", padding: "20px" }}>
      <div style={{ background: "#fff", padding: "20px" }}>
        {children}
      </div>
    </div>
  );
};

export default Modal;