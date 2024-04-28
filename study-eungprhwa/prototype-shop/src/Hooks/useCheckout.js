import { useContext } from "react";
import AppStateContext from "../Contexts/AppStateContext";

export default function useCheckout() {
  const { checkout } = useContext(AppStateContext);
  return { checkout };
}
