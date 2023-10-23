import { useNavigate } from "react-router";
import usePrototypes from "../Hooks/usePrototypes";

export default function CheckoutOrders(props) {
  const prototypes = usePrototypes();
  const navigate = useNavigate();
  const orders = props.orders;
  const totalPrice = props.totalPrice;
  
  return (
    <div className="order">
      <div className="body">
        {orders.map((order) => {
          const { id } = order;
          const prototype = prototypes.find((p) => p.id === id);
          return (
            <div className="item" key={id}>
              <div className="img">
                <video src={prototype.thumbnail} />
              </div>
              <div className="content">
                <p className="title">
                  {prototype.title} x {order.quantity}
                </p>
              </div>
              <div className="action">
                <p className="price">${prototype.price * order.quantity}</p>
              </div>
            </div>
          );
        })}
      </div>
      <div className="total">
        <hr />
        <div className="item">
          <div className="content">Total</div>
          <div className="action">
            <div className="price">${totalPrice}</div>
          </div>
        </div>
        <button
          className="btn btn--secondary"
          style={{ width: "100%", marginTop: 10 }}
          onClick={() => {
            alert("Payment Successful");
            navigate("/");
          }}
        >
          Pay
        </button>
      </div>
    </div>
  );
}
