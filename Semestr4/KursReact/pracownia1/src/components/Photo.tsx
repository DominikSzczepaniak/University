export default function Photo() {
    const style = {
      padding: "2px",
      border: "5px solid black",
      borderRadius: "90px",
      overflow: "hidden",
    };
    return (
      <div className="Photo">
        <img
          src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg"
          style={style}
          alt="A cute orange cat lying on its back."
        />
      </div>
    );
  }
  