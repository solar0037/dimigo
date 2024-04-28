import { useNavigate } from "react-router";
import { useMemo } from "react/cjs/react.development";
import useActions from "../Hooks/useActions";
import useOrders from "../Hooks/useOrders";
import usePrototypes from "../Hooks/usePrototypes";

export default function Orders() {
  const orders = useOrders();
  const prototypes = usePrototypes();
  const { remove, removeAll } = useActions();
  const navigate = useNavigate();
  const totalPrice = useMemo(() => {
    return orders
      .map((order) => {
        const { id, quantity } = order;
        const prototype = prototypes.find((p) => p.id === id);
        return prototype.price * quantity;
      })
      .reduce((l, r) => l + r, 0);
  }, [orders, prototypes]);
  // console.log(orders);

  if (orders.length === 0) {
    return (
      <aside>
        <div className="empty">
          <div className="title">장바구니에 상품이 없습니다.</div>
          <div className="subtitle">상품을 추가하려면 +버튼을 누르세요.</div>
        </div>
      </aside>
    );
  }

  return (
    <aside>
      <div className="order">
        <div className="body">
          {orders.map((order) => {
            const { id } = order;
            const prototype = prototypes.find((p) => p.id === id);
            const click = () => {
              remove(id);
            };
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
                  <button className="btn btn--link" onClick={click}>
                    <i className="icon icon--cross"></i>
                  </button>
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
            <button className="btn btn--link" onClick={removeAll}>
              <i className="icon icon--delete" />
            </button>
          </div>
          <button
            className="btn btn--secondary"
            style={{ width: "100%", marginTop: 10 }}
            onClick={() => {
              navigate("/checkout", {
                state: {
                  orders,
                  totalPrice,
                },
                replace: true,
              });
            }}
          >
            Checkout
          </button>
        </div>
      </div>
    </aside>
  );
}
