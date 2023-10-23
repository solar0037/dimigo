// import { useContext } from "react";
// import AppStateContext from "../Contexts/AppStateContext";
import useActions from '../Hooks/useActions';
import usePrototypes from "../Hooks/usePrototypes";

export default function Prototypes() {
  // const { prototypes } = useContext(AppStateContext);
  const prototypes = usePrototypes();
  const {addToOrder} = useActions();
  return (
    <main>
      <div className="prototypes">
        {prototypes.map((prototype) => {
          const { id, thumbnail, title, price, desc, pieUrl } = prototype;
          const click = () => {
            addToOrder(id);
          }
          return (
            <div className="prototype" key={id}>
              <a href={pieUrl} target="_blank" rel="noreferrer">
                <div>
                  <div
                    style={{
                      paddding: "25px 0 33px 0",
                    }}
                  >
                    <video
                      autoPlay
                      loop
                      playsInline
                      className="prototype__artwork prototype__edit"
                      src={thumbnail}
                    />
                  </div>
                </div>
              </a>
              <div className="prototype__body">
                <div className="prototype__title">
                  <div className="btn btn--primary float--right" onClick={click}>
                    <i className="icon icon--plus" />
                  </div>
                  {title}
                </div>
                <p className="prototype__price">${price}</p>
                <p className="prototype__desc">{desc}</p>
              </div>
            </div>
          );
        })}
      </div>
    </main>
  );
}
