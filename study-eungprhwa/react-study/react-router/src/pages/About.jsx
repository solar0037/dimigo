import queryString from 'query-string';

export default function About(props) {
    const searchParmas = props.location.search;
    // const obj = new URLSearchParams(searchParmas);
    const query = queryString.parse(searchParmas);
    return <div>About 페이지입니다.
        <br/>
        {/* name: {obj.get('name')}
        age: {obj.get('age')}
        grade: {obj.get('grade')} */}
        name: {query.name}
        age: {query.age}
        grade: {query.grade}
    </div>
}
