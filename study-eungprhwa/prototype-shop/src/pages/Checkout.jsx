import { useLocation } from "react-router";
import Header from "../components/Header";
import CheckoutMessage from "../components/CheckoutMessage";
import Footer from "../components/Footer";
import CheckoutOrders from "../components/CheckoutOrders";
import WrongRequest from "../components/WrongRequest";

function Checkout() {
  const location = useLocation();
  const orders = (() => {
    try {
      return location.state.orders;
    } catch {
      return null;
    }
  })();
  const totalPrice = (() => {
    try {
      return location.state.totalPrice;
    } catch {
      return null;
    }
  })();

  if (orders === null) {
    return (
      <>
        <Header />
        <WrongRequest />
        <Footer />
      </>
    );
  }

  return (
    <>
      <Header />
      <div className="container">
        <CheckoutMessage />
        <CheckoutOrders orders={orders} totalPrice={totalPrice} />
        <Footer />
      </div>
    </>
  );
}

export default Checkout;
