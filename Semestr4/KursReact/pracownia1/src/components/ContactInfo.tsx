interface IProps {
    phoneNumber: number;
    email: string;
    github: string;
  }
  
  export default function ContactInfo(props: IProps) {
    return (
      <div className="ContactInfo">
        <div className="Section">
          <img
            src="https://cdn2.iconfinder.com/data/icons/font-awesome/1792/phone-512.png"
            style={{ width: "30px", height: "30px" }}
          />
          <p>{props.phoneNumber}</p>
        </div>
        <div className="Section">
          <img
            src="https://e7.pngegg.com/pngimages/84/558/png-clipart-email-computer-icons-icon-design-message-email-miscellaneous-angle-thumbnail.png"
            style={{ width: "30px", height: "30px" }}
          />
          <p>{props.email}</p>
        </div>
        <div className="Section">
          <img
            src="https://w7.pngwing.com/pngs/646/324/png-transparent-github-computer-icons-github-logo-monochrome-head-thumbnail.png"
            style={{ width: "30px", height: "30px" }}
          />
          <p>{props.github}</p>
        </div>
      </div>
    );
  }
  