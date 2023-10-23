export default function Profile(props) {
    // const id = props.match.params.id;
    const id = props.location.search;
    return <div>Profile 페이지입니다.
        <br/>
        { id && <span> id는 {id}입니당. </span> }
    </div>
}
