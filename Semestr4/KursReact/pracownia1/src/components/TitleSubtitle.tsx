import React from "react";
import "../styles.css";

interface IProps {
  title: string;
  subtitle?: string;
  titleFontSize?: number;
  subtitleFontSize?: "number";
  color?: string;
}

export default function TitleSubtitle(props: IProps) {
  const titleStyle = {
    fontSize: props.titleFontSize ? `${props.titleFontSize}px` : "inherit",
    color: props.color ? props.color : "inherit",
  };
  const subtitleStyle = {
    fontSize: props.subtitleFontSize
      ? `${props.subtitleFontSize}px`
      : "inherit",
    color: props.color ? props.color : "inherit",
  };
  return (
    <div className="TitleSubtitle">
      <h1 style={titleStyle}>{props.title}</h1>
      {props.subtitle && <h2 style={subtitleStyle}>{props.subtitle}</h2>}
    </div>
  );
}
