import React from 'react';
import { useState } from 'react';
import * as Tabs from '@radix-ui/react-tabs';
import * as Switch from '@radix-ui/react-switch';
import * as Slider from '@radix-ui/react-slider';
import * as Label from '@radix-ui/react-label';
import * as Select from '@radix-ui/react-select';
import * as RadioGroup from '@radix-ui/react-radio-group';
import { Text } from '@radix-ui/themes';
import { CheckIcon, ChevronDownIcon, ChevronUpIcon } from '@radix-ui/react-icons';
import classnames from 'classnames';
import './App.css';
import './css/Radio.css';
import './css/Select.css'
import './css/Switch.css'
import './css/Tabs.css'
import './css/Slider.css'


const TabsDemo = () => {
  const [name, setName] = useState("");
  const [userName, setUserName] = useState("");
  const [gender, setGender] = useState("");
  const [password, setPassword] = useState("");
  const [notificationSetting, setNotificationSetting] = useState("");
  const [notificationFrequency, setNotificationFrequency] = useState(50);
  const [additionalDataCollection, setAdditionalDataCollection] = useState(false);

  const [draftname, setdraftName] = useState("");
  const [draftuserName, setdraftUserName] = useState("");
  const [draftgender, setdraftGender] = useState("");
  const [draftpassword, setdraftPassword] = useState("");
  const [draftnotificationSetting, setdraftNotificationSetting] = useState("");
  const [draftnotificationFrequency, setdraftNotificationFrequency] = useState(50);
  const [draftadditionalDataCollection, setdraftAdditionalDataCollection] = useState(false);

  const handledraftNameChange = (e) => {
    setdraftName(e.target.value);
  }

  const handledraftUserNameChange = (e) => {
    setdraftUserName(e.target.value);
  }

  const handledraftGenderChange = (e) => {
    setdraftGender(e.target.value);
  }

  const handledraftPasswordChange = (e) => {
    setdraftPassword(e.target.value);
  }

  const handledraftNotificationSettingChange = (e) => {
    setdraftNotificationSetting(e.target.value);
  }

  const handledraftNotificationFrequencyChange = (e) => {
    setdraftNotificationFrequency(e.target.value);
  }

  const handledraftAdditionalDataCollectionChange = (e) => {
    setdraftAdditionalDataCollection(e.target.value);
  }

  const saveDataAccount = () => {
    setName(draftname);
    setUserName(draftuserName);
    setGender(draftgender);
  }

  const saveDataPassword = () => {
    setPassword(draftpassword);
  }

  const saveDataPreferences = () => {
    setNotificationSetting(draftnotificationSetting);
    setNotificationFrequency(draftnotificationFrequency);
    setAdditionalDataCollection(draftadditionalDataCollection);
  }

  return (
  <Tabs.Root className="TabsRoot" defaultValue="tab1" orientation="vertical">
    <Tabs.List className="TabsList" aria-label="Manage your account">
      <Tabs.Trigger className="TabsTrigger" value="tab1">
        Account
      </Tabs.Trigger>
      <Tabs.Trigger className="TabsTrigger" value="tab2">
        Password
      </Tabs.Trigger>
      <Tabs.Trigger className="TabsTrigger" value="tab3">
        Preferences
      </Tabs.Trigger>
    </Tabs.List>
    <Tabs.Content className="TabsContent" value="tab1">
      <Text className="Text">Make changes to your account here. Click save when you're done.</Text>
      <fieldset className="Fieldset">
        <Label.Root className="Label" htmlFor="name">
          Name
        </Label.Root>
        <input className="Input" id="name" defaultValue={name} onChange={handledraftNameChange}/>
      </fieldset>
      <fieldset className="Fieldset">
        <Label.Root className="Label" htmlFor="username">
          Username
        </Label.Root>
        <input className="Input" id="username" defaultValue={userName} onChange={handledraftUserNameChange}/>
      </fieldset>
      <fieldset className="Fieldset">
        <Label.Root className="Label" htmlFor="Gender">
          Gender
        </Label.Root>
        <RadioGroup.Root className="RadioGroupRoot" defaultValue="default" aria-label="View density" onChange={handledraftGenderChange}>
      <div style={{ display: 'flex', alignItems: 'center' }}>
        <RadioGroup.Item className="RadioGroupItem" value="male" id="r1">
          <RadioGroup.Indicator className="RadioGroupIndicator" />
        </RadioGroup.Item>
        <Label.Root className="LabelRadio" htmlFor="r1">
          Male
        </Label.Root>
      </div>
      <div style={{ display: 'flex', alignItems: 'center' }}>
        <RadioGroup.Item className="RadioGroupItem" value="female" id="r2">
          <RadioGroup.Indicator className="RadioGroupIndicator" />
        </RadioGroup.Item>
        <Label.Root className="LabelRadio" htmlFor="r2">
          Female
        </Label.Root>
      </div>
      <div style={{ display: 'flex', alignItems: 'center' }}>
        <RadioGroup.Item className="RadioGroupItem" value="other" id="r3">
          <RadioGroup.Indicator className="RadioGroupIndicator" />
        </RadioGroup.Item>
        <Label.Root className="LabelRadio" htmlFor="r3">
          Other
        </Label.Root>
      </div>
    </RadioGroup.Root>

      </fieldset>
      <div style={{ display: 'flex', marginTop: 20, justifyContent: 'flex-end' }}>
        <button className="Button green" onClick={saveDataAccount}>Save changes</button>
      </div>
    </Tabs.Content>
    <Tabs.Content className="TabsContent" value="tab2">
      <Text className="Text">Change your password here. After saving, you'll be logged out.</Text>
      <fieldset className="Fieldset">
        <Label.Root className="Label" htmlFor="currentPassword">
          Current password
        </Label.Root>
        <input className="Input" id="currentPassword" type="password"/>
      </fieldset>
      <fieldset className="Fieldset">
        <Label.Root className="Label" htmlFor="newPassword">
          New password
        </Label.Root>
        <input className="Input" id="newPassword" type="password" onChange={handledraftPasswordChange}/>
      </fieldset>
      <fieldset className="Fieldset">
        <Label.Root className="Label" htmlFor="confirmPassword">
          Confirm password
        </Label.Root>
        <input className="Input" id="confirmPassword" type="password" />
      </fieldset>
      <div style={{ display: 'flex', marginTop: 20, justifyContent: 'flex-end' }}>
        <button className="Button green" onClick={saveDataPassword}>Change password</button>
      </div>
    </Tabs.Content>
    <Tabs.Content className="TabsContent" value="tab3">
      <Text className="Text">Change your preferences here. Click save when you're done.</Text>
      <fieldset className="Fieldset">
        <Label.Root className="Label" htmlFor="notificationSettings">
          Notification settings
        </Label.Root>
        <Select.Root>
          <Select.Trigger className="SelectTrigger" aria-label="Food" onChange={handledraftNotificationSettingChange}>
            <Select.Value className="SelectValue" placeholder={notificationSetting} />
            <Select.Icon className="SelectIcon">
              <ChevronDownIcon />
            </Select.Icon>
          </Select.Trigger>
          <Select.Portal>
            <Select.Content className="SelectContent">
              <Select.ScrollUpButton className="SelectScrollButton">
                <ChevronUpIcon />
              </Select.ScrollUpButton>
              <Select.Viewport className="SelectViewport">
                <Select.Group>
                  <SelectItem value="all">All</SelectItem>
                  <SelectItem value="onlyFollowed">Only followed</SelectItem>
                  <SelectItem value="None">None</SelectItem>
                </Select.Group>
              </Select.Viewport>
              <Select.ScrollDownButton className="SelectScrollButton">
                <ChevronDownIcon />
              </Select.ScrollDownButton>
            </Select.Content>
          </Select.Portal>
        </Select.Root>
      </fieldset>
      <fieldset className="Fieldset">
        <Label.Root className="Label" htmlFor="notificationFrequency" onChange={handledraftNotificationFrequencyChange}>
          Notification Frequency
        </Label.Root>
        <Slider.Root className="SliderRoot" defaultValue={[50]} max={100} step={1}>
          <Slider.Track className="SliderTrack">
            <Slider.Range className="SliderRange" />
          </Slider.Track>
          <Slider.Thumb className="SliderThumb" aria-label="Volume" />
        </Slider.Root>
      </fieldset>
      <fieldset className="Fieldset">
        <Label.Root className="Label" htmlFor="additionDataCollection" onChange={handledraftAdditionalDataCollectionChange}>
          Collect additional data
        </Label.Root>
        <Switch.Root className="SwitchRoot" id="airplane-mode">
          <Switch.Thumb className="SwitchThumb" />
        </Switch.Root>

      </fieldset>
      <div style={{ display: 'flex', marginTop: 20, justifyContent: 'flex-end' }}>
        <button className="Button green" onClick={saveDataPreferences}>Save preferences</button>
      </div>


    </Tabs.Content>
  </Tabs.Root>
)};

const SelectItem = React.forwardRef(({ children, className, ...props }, forwardedRef) => {
  return (
    <Select.Item className={classnames('SelectItem', className)} {...props} ref={forwardedRef}>
      <Select.ItemText>{children}</Select.ItemText>
      <Select.ItemIndicator className="SelectItemIndicator">
        <CheckIcon />
      </Select.ItemIndicator>
    </Select.Item>
  );
});


export default TabsDemo;
