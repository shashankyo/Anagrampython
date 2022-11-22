import logo from './logo.svg';
import './App.css';
const stories =[
  {
  title:'React',
  url:'https://reactjs.org/',
  author:'Jordan Walke',
  num_comments:3,
  points:4,
  objectID:0,
  },
  {
    title:'Redux',
    url:'https://redux.js.org/',
    author:'Dan Abramov,Andrew Clark',
    num_comments:2,
    points:5,
    objectID:1,
    },
];
const [searchTerm, setSearchTerm] = React.usestate('');

const handleSearch = (event) => {
  setSearchTerm(event.target.value);
};

  return (
    <div>
      <h1>MY Hcker Stories</h1>

      <search onSearch = {handleSearch} />
      <hr />
      <List list={stories} />
      </div>
      );
      

      const Search = (props) => (
        <div>
            <label htmlFor="search">Search:</label>
            <input id="search" type="text" onChange={props.onSearch} />
        </div>
      );
    


