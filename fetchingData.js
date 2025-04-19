import React from "react";
import { useEffect, useState } from "react";

/**
1. import useEffect, useState
2. add a post state variable with useState
3. add the baseurl
4. create a useEffect hook, inside that hook
      -create a fetch function async
      -create a response
      -transform the data into .json 
      -setting the post variable to the transformed data
      -address if there are errorrs
      -address loading

      outside the function but inside of the hook, call the function
      -check if there are any dependencies
 */
const BASE_URL = "https://jsonplaceholder.typicode.com";

export function App() {
  const [posts, setPosts] = useState([]);
  const [errors, setErrors] = useState();
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch(`${BASE_URL}/posts`); //you forgot the fetch!
      const posts = await response.json();
      console.log(posts);
      setPosts(posts);
    };
    fetchData();
  }, []);
  return (
    <div className="App">
      <h1>Fetch Posts</h1>
      <h2>See all of the posts below!</h2>
      <ul>
        {posts.map((post) => (
          <li key={post.id}>
            {post.title}
            {post.body}
          </li>
        ))}
      </ul>
    </div>
  );
}

// Log to console
console.log("Hello console");

export default fetchingData;
