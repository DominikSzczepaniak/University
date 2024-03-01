interface IProps {
    title: string;
  }
  export function Skills(props: IProps) {
    return (
      <div className="Skills">
        <h1
          style={{
            backgroundColor: "#32333b",
            color: "#797b91",
            borderRadius: "20px",
            padding: "7px",
            display: "inline-block",
          }}
        >
          {props.title}
        </h1>
      </div>
    );
  }
  